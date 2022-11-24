from datacenter.models import Visit, format_duration
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)

    for visit in visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
