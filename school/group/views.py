from django.http import JsonResponse

from group.models import Group


def get_groups(request):
    groups = [
        {
            'group_name': group.group_name,
            'group_direction': group.number_of_group_members,
            'group_size': group.group_type

        }
        for group in Group.objects.all()
    ]

    data = {
        'count': Group.objects.count(),
        'groups': groups,
    }

    return JsonResponse(data)