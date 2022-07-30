from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
# Create your views here.
from User import models


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj_user = models.WangUser.objects.filter(username=username, password=password)
        print(username)

        print(obj_user)
        if obj_user:
            return render(request, 'index.html', {'username': username})
        error = '用户名和密码错误'

    return render(request, 'login.html', locals(), )


@login_required
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_list = models.WangUser.objects.filter(username=username)
        error_name = []
        if user_list:
            error_name = '用户名已经存在'
            return render(request, 'register.html', {'error_name': error_name})
        else:
            username = models.WangUser.objects.create(username=username, password=password, email=email)
            username.save()
            return redirect('login')
    return render(request, 'register.html')


# Create your views here.


def setting(request):
    user = models.WangUser.objects.get(username=15210958305)
    print(user)
    return render(request, 'setting.html',{'username':user})

def personal_homepage(request):
    return render(request,'personal_homepage.html')

# 查询所有数据
def list_dep_old(request):
    # 查询所有数据
    def_list=models.department.objects.all()#查询方法：all(),filter(),exclude(),get()
    return render(request,'list_dep_old.html',{'dep_list':def_list})
#添加数据
def add_dep_old(request):
    # 判断请求方式，如果post，说明前端需要提交数据
    if request.method=='POST':
        # 获取传过来的get()函数中的参数（html文件input（）标签的name属性）
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
    # strip()过滤
        if dep_name.strip()=='':
            return render(request,'add_dep_old.html',{'error_info':'名称不能为空'})
        # 用create（）函数新建一条函数，会自动保存，不需要调用save（）函数
        try:
            # 添加数据有两种方式：1.使用模型管理器的create（）方法添加数据，2.使用模型实列save（）方法保存
            p=department.objects.create(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            return render(request,'test_orm_old/add_dep_old.html',{'error_info':'输入部门名称重复或信息错误！'})
        finally:
            pass
    return render(request,'test_orm_old/add_dep_old.html/')
#删除数据
def del_dep_old(request,dep_id):
    dep_object=department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old/')
#修改数据
def edit_dep_old(request,dep_id):
    if request.method=='POST':
        id=request.POST.get('id')
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
        dep_object=department.objects.get(id=id)
        dep_object.dep_name=dep_name
        dep_object.dep_script=dep_script
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object=department.objects.get(id=dep_id)
        return render(request,'test_orm_old/edit_dep_old.html',{'department':dep_object})

