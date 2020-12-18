from django.http import HttpResponse
from django.shortcuts import redirect

def user_is_authenticated(views_file):
    def inshid_func_name(request, *args, **kwargs):
        """
        here the write conditions inside the functions
        """
        if request.user.is_authenticated:
            return redirect('cust_home')
        else:
            return views_file(request, *args, **kwargs)        
    return inshid_func_name



# this deco for who can access the particular pages
def allowed_user(allowed_rolls = []):
    def deco(view_file):
        """
        here the 'deco' for rolls
        """
        def inshid_rols_code(request, *args, **kwargs):
            """
            here the part is 'views file code to execute'
            """
            # here the logic
            # print("working", allowed_rolls)

            group = None

            # here the we check the user is exists in gropu
            if request.user.groups.exists():
                # here the we check in group
                # users 1st index name is 'admin' 
                group = request.user.groups.all()[0].name
                # ok here the we got 'admin' role
                # note: you can't understand then go to views.py and see the 'deco' of allowed_user line

            if group in allowed_rolls:
                return view_file(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to views this page')
        return inshid_rols_code
    return deco


# this deco for admin
def admin_only(view_file):
    def admin_can_do(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return redirect('userpage')
        
        if group == 'admin':
            return view_file(request, *args, **kwargs)
    return admin_can_do