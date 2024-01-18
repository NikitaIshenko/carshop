from django.shortcuts import render, redirect

def main(request):
    return redirect("automobile:index")

