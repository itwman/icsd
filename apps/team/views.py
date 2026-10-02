from django.shortcuts import get_object_or_404, render

from .models import TeamMember


def team_list(request):
    members = TeamMember.objects.filter(is_active=True)
    return render(request, "team/team_list.html", {"members": members})


def member_detail(request, slug):
    m = get_object_or_404(TeamMember.objects.prefetch_related("education", "experience", "publications", "skills", "socials"),
                          slug=slug, is_active=True)
    return render(request, "team/member_detail.html", {"m": m, "seo_obj": m})
