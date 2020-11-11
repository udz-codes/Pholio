from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("about", views.about_view, name="about"),

    # Main Page and User Portfolio
    path("<str:username>", views.portfolio, name="portfolio"),
    # path("user", views.my_view, name="my_view"),

    # CRUD stuff
    path("user/profile", views.profile, name="profile"),
        # Introduction
    path("user/profile/introduction", views.intro_view, name="introduction"),

        # Socials
    path("user/profile/socials", views.socials, name="socials"),
        # Experience
    path("user/profile/experience/<int:exp_id>", views.experience_view, name="experience"),
    path("user/profile/addExperience", views.add_experience, name="addExperience"),

        # Project
    path("user/profile/project/<int:proj_id>", views.project_view, name="project"),
    path("user/profile/addProject", views.add_project, name="addProject"),

        # Education
    path("user/profile/education/<int:edu_id>", views.education_view, name="education"),
    path("user/profile/addEducation", views.add_education, name="addEducation"),

        # Skills
    path("user/profile/addSkill/<int:cat_id>", views.skills_view, name="addSkill"),
    path("user/profile/delSkill/<int:skill_id>", views.del_skill, name="delSkill"),

        # Certifications
    path("user/profile/certificate/<int:cert_id>", views.certificate_view, name="certificate"),
    path("user/profile/addCertificate", views.add_certificate, name="addCertificate"),

        # Sections
    path("user/profile/section", views.sections_toggle, name="sectionsToggle"),

        # Password reset
    path("user/reset_password/", auth_views.PasswordResetView.as_view(template_name="pholio/pass_reset.html"), name="reset_password"), # Submit email form
    path("user/reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="pholio/pass_reset_sent.html"), name="password_reset_done"), # Email sent success message
    path("user/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="pholio/pass_reset_form.html"), name="password_reset_confirm"), # Link to password reset form in email
    path("user/reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="pholio/pass_reset_done.html"), name="password_reset_complete"), # Password successfully changes message
]