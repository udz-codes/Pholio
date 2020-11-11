import json
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import User, Profile, Social, Experience, Project, Education, Certification, SkillCategory, Skill, Sections
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):

    if request.user.is_authenticated:

        data = Profile.objects.get(user=request.user)

        return HttpResponseRedirect(reverse("portfolio", kwargs={
            "username": data.username
        }))
    else:
        return render(request, "pholio/index.html")

def about_view(request):
    return render(request, "pholio/about.html")

def socials(request):

    try:
        socials = Social.objects.get(user=request.user)
    except Social.DoesNotExist:
        return JsonResponse({"error": "User's socials not found."}, status=404)

    if request.method == "POST":

        if request.POST["linkedin"] == '':
            socials.linkedin = None
        else:
            if "https://" in request.POST["linkedin"]:
                linkdn = request.POST["linkedin"]
            else:
                linkdn = "https://" + request.POST["linkedin"]
            
            socials.linkedin = linkdn
        
        if request.POST["github"] == '':
            socials.github = None
        else:
            if "https://" in request.POST["github"]:
                githb = request.POST["github"]
            else:
                githb = "https://" + request.POST["github"]

            socials.github = githb
        
        if request.POST["twitter"] == '':
            socials.twitter = None
        else:
            if "https://" in request.POST["twitter"]:
                twtr = request.POST["twitter"]
            else:
                twtr = "https://" + request.POST["twitter"]

            socials.twitter = twtr

        socials.save()

        return HttpResponseRedirect(reverse("profile"))


@csrf_exempt
@login_required
def skills_view(request, cat_id):

    try:
        category = SkillCategory.objects.get(pk=cat_id)
    except SkillCategory.DoesNotExist:
        return JsonResponse({"error": "Skill Category not found."}, status=404)

    if request.method == "POST":

        data = json.loads(request.body)

        if str.strip(data["name"]) != "":
            skill = Skill(user=request.user, category=category, name=str.strip(data["name"]))

            skill.save()

            newskill = Skill.objects.get(user=request.user, category=category, name=str.strip(data["name"]))

            return JsonResponse({
                "message": f"{newskill.pk}"
            })


@csrf_exempt
@login_required
def del_skill(request, skill_id):

    try:
        skill = Skill.objects.get(pk=skill_id)
    except Skill.DoesNotExist:
        return JsonResponse({"error": "Skill not found."}, status=404)

    if request.method == "POST":

        skill.delete()

        return HttpResponse(status=204)


@csrf_exempt
@login_required
def intro_view(request):

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return JsonResponse({"error": "Profile not found."}, status=404)

    if request.method == "PUT":

        data = json.loads(request.body)

        profile.name = data["name"]
        profile.title = data["title"]
        profile.about = data["about"]

        profile.save()

        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)


@csrf_exempt
@login_required
def experience_view(request, exp_id):

    try:
        experience = Experience.objects.get(pk=exp_id)
    except Experience.DoesNotExist:
        return JsonResponse({"error": "Experience not found."}, status=404)

    if request.method == "PUT":

        data = json.loads(request.body)

        experience.title = data["title"]
        experience.company = data["company"]
        experience.startdate = data["startdate"]
        experience.enddate = data["enddate"]
        experience.description = data["description"]

        experience.save()

        return HttpResponse(status=204)

    elif request.method == "POST":
        
        experience.delete()

        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "PUT and POST request required."
        }, status=400)


@csrf_exempt
@login_required
def project_view(request, proj_id):

    try:
        project = Project.objects.get(pk=proj_id)
    except Project.DoesNotExist:
        return JsonResponse({"error": "Project not found."}, status=404)

    if request.method == "PUT":

        data = json.loads(request.body)

        project.title = data["title"]
        project.startdate = data["startdate"]
        project.enddate = data["enddate"]
        project.description = data["description"]

        git = ""
        if data["github"] != "":
            if "https://" in data["github"]:
                git = data["github"]
            else:
                git = "https://" + data["github"]

        print(data["website"])

        web = ""
        if data["website"] != "":
            if "https://" in data["website"]:
                web = data["website"]
            else:
                web = "https://" + data["website"]

        project.github = git
        project.website = web

        project.save()

        return HttpResponse(status=204)

    elif request.method == "POST":
        
        project.delete()

        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "PUT and POST request required."
        }, status=400)


@csrf_exempt
@login_required
def education_view(request, edu_id):

    try:
        education = Education.objects.get(pk=edu_id)
    except Education.DoesNotExist:
        return JsonResponse({"error": "Education not found."}, status=404)

    if request.method == "PUT":

        data = json.loads(request.body)

        education.title = data["title"]
        education.startyear = data["startYear"]
        education.endyear = data["endYear"]
        education.description = data["description"]

        education.field = data["field"]
        education.school = data["school"] 

        education.save()

        return HttpResponse(status=204)

    elif request.method == "POST":
        
        education.delete()

        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "PUT and POST request required."
        }, status=400)


@csrf_exempt
@login_required
def certificate_view(request, cert_id):

    try:
        certification = Certification.objects.get(pk=cert_id)
    except Certification.DoesNotExist:
        return JsonResponse({"error": "Certification not found."}, status=404)

    if request.method == "PUT":

        data = json.loads(request.body)

        certification.title = data["title"]
        certification.organisation = data["organisation"]
        certification.date = data["date"]
        certification.credential = data["credential"]

        link=""
        if data["link"] != "":
            if "https://" in data["link"]:
                link = data["link"]
            else:
                link = "https://" + data["link"]
        
        certification.certificate = link

        certification.save()

        return HttpResponse(status=204)

    elif request.method == "POST":
        
        certification.delete()

        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "PUT and POST request required."
        }, status=400)


@csrf_exempt
@login_required
def add_experience(request):

    if request.method == "POST":

        data = json.loads(request.body)

        experience = Experience(user=request.user, title=data["title"], company=data["company"], startdate=data["startdate"], enddate=data["enddate"], description=data["description"] )
        experience.save()

        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


@csrf_exempt
@login_required
def add_project(request):

    if request.method == "POST":

        data = json.loads(request.body)

        git = ""
        if data["github"] != "":
            if "https://" in data["github"]:
                git = data["github"]
            else:
                git = "https://" + data["github"]

        web = ""
        if data["website"] != "":
            if "https://" in data["website"]:
                web = data["website"]
            else:
                web = "https://" + data["website"]

        project = Project(user=request.user, title=data["title"], startdate=data["startdate"], enddate=data["enddate"], description=data["description"], github=git, website=web)
        project.save()

        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


@csrf_exempt
@login_required
def add_education(request):

    if request.method == "POST":

        data = json.loads(request.body)

        education = Education(user=request.user, title=data["title"], startyear=data["startyear"], endyear=data["endyear"], description=data["description"], field=data["field"], school=data["school"])
        education.save()

        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


@csrf_exempt
@login_required
def add_certificate(request):

    if request.method == "POST":

        data = json.loads(request.body)

        link = ""
        if data["link"] != "":
            if "https://" in data["link"]:
                link = data["link"]
            else:
                link = "https://" + data["link"]

        certificate = Certification(user=request.user, title=data["title"], organisation=data["organisation"], credential=data["credential"], date=data["date"], certificate=link)
        certificate.save()

        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)



def portfolio(request, username):

    # ----------------------- User Data
    try:
        data = Profile.objects.get(username=username)
    except Profile.DoesNotExist:
        data = None

        return render(request, "pholio/nouser.html",{
            "username": username,
        })

    # ----------------------- Get user
    try:
        user = User.objects.get(username=data.email)
    except User.DoesNotExist:
        user = None

    # ----------------------- User Socials
    try:
        socials = user.social.get()
    except:
        socials = None

    # ----------------------- Sections
    try:
        section_items = user.sections.all()
    except:
        section_items = None

    sections = []

    if section_items:
        for section in section_items or []:
            sections = section
    
    # ----------------------- User Experiences
    if sections.experience  :
        try:
            experiences = user.experience.all().order_by('-startdate')
        except:
            experiences = None

        if experiences:
            for experience in experiences or []:

                experience.startdate = experience.startdate.strftime("%B %Y")
                
                if experience.enddate:
                    experience.enddate = experience.enddate.strftime("%B %Y")
                else:
                    experience.enddate = None
    else:
        experiences = None

    # ----------------------- User Projects
    if sections.projects:
        try:
            projects = user.project.all().order_by('-startdate')
        except:
            projects = None

        if projects:
            for project in projects or []:

                project.startdate = project.startdate.strftime("%B %Y")
                
                if project.enddate:
                    project.enddate = project.enddate.strftime("%B %Y")
                else:
                    project.enddate = None
    else:
        projects = None

    # ----------------------- User Education
    if sections.education:
        try:
            educations = user.education.all().order_by('-startyear')
        except:
            educations = None
    else:
        educations = None
    # ----------------------- User Certifications
    if sections.certifications:
        try:
            certifications = user.certificte.all().order_by('-date')
        except:
            certifications = None

        if certifications:
            for certification in certifications or []:

                certification.date = certification.date.strftime("%B %Y")
    else:
        certifications = None

    # ----------------------- All Categories
    if sections.skills:
        try:
            skillCategories = SkillCategory.objects.all()
        except:
            skillCategories = None

        try:
            skills = user.skills.all()
        except:
            skills = None
    else:
        skillCategories = None
        skills = None

    return render(request, "pholio/portfolio.html",{
        "data": data,
        "sections": sections,
        "socials": socials,
        "experiences": experiences,
        "projects": projects,
        "educations": educations,
        "certifications": certifications,
        "skillCategories": skillCategories,
        "skills": skills,
    })


@login_required
def profile(request):

    user_c = request.user

    # ----------------------- User Data
    try:
        data = Profile.objects.get(user=user_c)
    except:
        data = None

    # ----------------------- User Socials
    try:
        socials = user_c.social.get()
    except:
        socials = None

    # ----------------------- User Experiences
    try:
        experiences = Experience.objects.filter(user=user_c).all().order_by('-startdate')

    except:
        experiences = None

    for experience in experiences or []:

        experience.startdate = experience.startdate.strftime("%d-%m-%Y")
        
        if experience.enddate:
            experience.enddate = experience.enddate.strftime("%d-%m-%Y")
        else:
            experience.enddate = None

    # ----------------------- User Projects
    try:
        projects = Project.objects.filter(user=user_c).all().order_by('-startdate')
    except:
        projects = None

    for project in projects or []:

        project.startdate = project.startdate.strftime("%d-%m-%Y")
        
        if project.enddate:
            project.enddate = project.enddate.strftime("%d-%m-%Y")
        else:
            project.enddate = None

    # ----------------------- User Education
    try:
        educations = Education.objects.filter(user=user_c).all().order_by('-startyear')
    except:
        educations = None

    # ----------------------- User Certifications
    try:
        certifications = Certification.objects.filter(user=user_c).all().order_by('-date')
    except:
        certifications = None

    for certificate in certifications or []:

        certificate.date = certificate.date.strftime("%d-%m-%Y")

    # ----------------------- All Categories
    try:
        skillCategories = SkillCategory.objects.all()
    except:
        skillCategories = None

    # ----------------------- User Certifications
    try:
        skills = Skill.objects.filter(user=user_c).all()
    except:
        skills = None

    try:
        section_items = Sections.objects.filter(user=user_c)
    except:
        section_items = None

    sections = []

    for section in section_items or []:
        sections = section

    return render(request, "pholio/profile.html",{
        "data": data,
        "socials": socials,
        "experiences": experiences,
        "projects": projects,
        "educations": educations,
        "certifications": certifications,
        "skillCategories": skillCategories,
        "skills": skills,
        "sections": sections
    })


@csrf_exempt
@login_required
def sections_toggle(request):

    try:
        sections = Sections.objects.get(user=request.user)
    except Sections.DoesNotExist:
        return JsonResponse({"error": "Sections model not found."}, status=404)

    if request.method == "POST":

        data = json.loads(request.body)

        section_name = data["section_name"]

        if section_name == 'about':
            if sections.about:
                sections.about = False

            elif not sections.about:
                sections.about = True

        elif section_name == 'experience':
            if sections.experience:
                sections.experience = False

            elif not sections.experience:
                sections.experience = True

        elif section_name == 'projects':
            if sections.projects:
                sections.projects = False

            elif not sections.projects:
                sections.projects = True

        elif section_name == 'education':
            if sections.education:
                sections.education = False

            elif not sections.education:
                sections.education = True

        elif section_name == 'skills':
            if sections.skills:
                sections.skills = False

            elif not sections.skills:
                sections.skills = True

        elif section_name == 'certifications':
            if sections.certifications:
                sections.certifications = False

            elif not sections.certifications:
                sections.certifications = True

        sections.save()

        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pholio/login.html", {
                "message": "Invalid email and/or password.",
                "type": "danger"
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pholio/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):

    if request.method == 'POST':
        email = request.POST["email"]
        name = request.POST["name"]
        uname = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "pholio/register.html", {
                "message": "Passwords must match.",
                "type": "danger"
            })

        profile_user = Profile.objects.filter(username=uname).count()

        if profile_user > 0:
            return render(request, "pholio/register.html", {
                "message": "Username already taken.",
                "type": "danger"
            })

        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "pholio/register.html", {
                "message": "Email address already taken.",
                "type": "warning"
            })

        login(request, user)

        profile = Profile(user=user, username=uname, name=name, email=email)
        profile.save()

        socials = Social(user=user)
        socials.save()

        sections = Sections(user=user)
        sections.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pholio/register.html")