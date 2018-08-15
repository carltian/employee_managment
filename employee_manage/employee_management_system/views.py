# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .models import Employee
# Create your views here.
def hello(request):#功能选择
    # t = loader.get_template("hello.html")
    # c = RequestContext(request)
    return render_to_response("hello.html",context_instance=RequestContext(request))

def addinfo(request):# 添加信息
    name            = request.POST.get("name")
    age             = request.POST.get("age")
    birth           = request.POST.get("birth")
    joinpartytime   = request.POST.get("joinpartytime")
    job             = request.POST.get("job")
    salary          = request.POST.get("salary")
    education       = request.POST.get("education")
    major           = request.POST.get("major")
    graduationtime  = request.POST.get("graduationtime")
    phonenumber     = request.POST.get("phonenumber")
    remark          = request.POST.get("remark")
    newemp          = Employee(name=name,age=age,birth=birth,joinpartytime=joinpartytime,job=job
                               ,salary=salary,education=education,major=major,graduationtime=graduationtime
                               ,phonenumber=phonenumber,remark=remark)
    newemp.save()
    # c = RequestContext(request)
    # t = loader.get_template("check.html")
    return render_to_response("done.html",context_instance=RequestContext(request,{
    'name': name,
    'age': age,
    'birth':birth,
    'joinpartytime':joinpartytime,
    'job':job,
    'salary':salary,
    'education':education,
    'major':major,
    'graduationtime':graduationtime,
    'phonenumber':phonenumber,
    'remark':remark,
    }))

def checkinfo(request):#查询学生信息
    find = []
    emplist = Employee.objects.all()
    name            = request.POST.get("name")
    age             = request.POST.get("age")
    birth           = request.POST.get("birth")
    joinpartytime   = request.POST.get("joinpartytime")
    job             = request.POST.get("job")
    salary          = request.POST.get("salary")
    education       = request.POST.get("education")
    major           = request.POST.get("major")
    graduationtime  = request.POST.get("graduationtime")
    phonenumber     = request.POST.get("phonenumber")
    remark          = request.POST.get("remark")
    if name:
        find = Employee.objects.filter(name__contains=name)
    elif age:
        find = Employee.objects.filter(age=age)
    elif birth:
        find = Employee.objects.filter(birth__contains=birth)
    elif joinpartytime:
        joinpartytime = Employee.objects.filter(joinpartytime__contains=joinpartytime)
    elif job:
        find = Employee.objects.filter(job__contains=job)
    elif salary:
        salary = Employee.objects.filter(salary=salary)
    elif education:
        education = Employee.objects.filter(education__contains=education)
    elif major:
        major = Employee.objects.filter(major__contains=major)
    elif graduationtime:
        graduationtime = Employee.objects.filter(graduationtime__contains=graduationtime)
    elif phonenumber:
        find = Employee.objects.filter(phonenumber=phonenumber)
    elif remark:
        remark = Employee.objects.filter(remark_contains=remark)


    return render_to_response("check.html",context_instance=RequestContext(request,{"emplist":emplist,"find":find}))

def putmessage(request):#信息提交中转
    return render_to_response("add.html",context_instance=RequestContext(request))

def deletemp(request):#删除信息
    alert=""
    name            = request.POST.get("name")
    age             = request.POST.get("age")
    birth           = request.POST.get("birth")
    joinpartytime   = request.POST.get("joinpartytime")
    job             = request.POST.get("job")
    salary          = request.POST.get("salary")
    education       = request.POST.get("education")
    major           = request.POST.get("major")
    graduationtime  = request.POST.get("graduationtime")
    phonenumber     = request.POST.get("phonenumber")
    remark          = request.POST.get("remark")
    delet = request.POST.get("delet")
    find = Employee.objects.filter(name__contains =name)
    if not find:
        alert = u"没有找到名为" + name + u"的学生"
    elif not delet:
        alert=""
    else:
        find.delete()
        alert = u"成功删除该学生"
    return render_to_response("delet.html",context_instance=RequestContext(request,{"alert":alert,"employee":find}))

def putmessage2(request):#信息提交中转2
    return render_to_response("put2.html",context_instance=RequestContext(request))


def rewrite(request):#信息更改
    aler=u"提示："
    emplist = Employee.objects.all()
    message = request.POST.get("message")
    old = request.POST.get("old")
    new = request.POST.get("new")
    if old == "name":
        employee= Employee.objects.filter( name__contains = message).update(name = new)
        aler+=u"信息修改成功"
    elif old== "age":
        employee= Employee.objects.filter( name__contains = message).update(age = new)
        aler+=u"信息修改成功"
    elif old =="birth":
        employee= Employee.objects.filter( name__contains = message).update(birth = new)
        aler+=u"信息修改成功"
    elif old == "joinpartytime":
        employee = Employee.objects.filter(name__contains=message).update(joinpartytime=new)
        aler += u"信息修改成功"
    elif old == "job":
        employee = Employee.objects.filter(name__contains=message).update(job=new)
        aler += u"信息修改成功"
    elif old == "salary":
        employee = Employee.objects.filter(name__contains=message).update(salary=new)
        aler += u"信息修改成功"
    elif old == "major":
        employee = Employee.objects.filter(name__contains=message).update(major=new)
        aler += u"信息修改成功"
    elif old == "graduationtime ":
        employee = Employee.objects.filter(name__contains=message).update(graduationtime =new)
        aler += u"信息修改成功"
    elif old == "phonenumber":
        employee = Employee.objects.filter(name__contains=message).update(phonenumber=new)
        aler += u"信息修改成功"
    elif old == "remark":
        employee = Employee.objects.filter(name__contains=message).update(remark=new)
        aler += u"信息修改成功"
    else:
        aler+=u"请输入正确的需要修改的信息类别"
    return render_to_response("show.html",context_instance=RequestContext(request,{"id":id,"message":message,"new":new,"emplist":emplist,"aler":aler}))