from django.shortcuts import render
from .models import LikeRecord, LikeCount
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist


# Create your views here.

def errorResponse(code, msg):
    data = {
        'status': 'ERROR',
        'code': code,
        'msg': msg,
    }
    return JsonResponse(data)


def successResponse(like_num):
    data = {
        'status': 'ERROR',
        'like_num': like_num,
    }
    return JsonResponse(data)


def like_change(requests):
    # 获取数据
    user = requests.user
    if not user.is_authenticated:
        return errorResponse(400, '你还没有登录')
    contrnt_type = requests.GET.get('content_type')
    object_id = int(requests.GET.get('object_id'))

    try:
        contrnt_type = ContentType.objects.get(contrnt_type=contrnt_type)
        model_class = contrnt_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist as e:
        return errorResponse(401, '对象不存在')

    # 处理数据
    if requests.GET.get('is_like') == 'true':
        # 用户点赞
        like_record, created = LikeRecord.objects.get_or_create(contrnt_type=contrnt_type, object_id=object_id)

        if created:
            # 没有点赞过
            like_count, created = LikeCount.objects.get_or_create(contrnt_type=contrnt_type, object_id=object_id)
            like_count.liked_num += 1
            like_count.save()
            return successResponse(like_count.liked_num)
        else:
            # 点赞过，不能重复点赞
            return errorResponse(402, '你已经点过赞了')
    else:
        # 用户取消点赞
        if LikeRecord.objects.filter(contrnt_type=contrnt_type, object_id=object_id, user=user).exists():
            # 有点赞过，取消点赞
            like_record = LikeRecord.objects.get(contrnt_type=contrnt_type, object_id=object_id)
            like_record.delete()
            # 点赞总数减1
            like_count, created = LikeCount.objects.get_or_create(content_type=contrnt_type, object_id=object_id)
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return successResponse(like_count.liked_num)
            else:
                return errorResponse(404, '数据错误')
        else:
            # 没有点赞过，不能取消
            return errorResponse(403, '你还没有点赞过')
