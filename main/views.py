from django.shortcuts import render
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from braille_board.settings import BASE_DIR
import os
from sklearn.model_selection import train_test_split

sns.set(color_codes=True)
data_frame = pd.read_csv(os.path.join(BASE_DIR, "pimadataorig.csv"))
# Create your views here.

def home(request):
    context = {
        "title": "Pregnancy Model"
    }
    if request.method == "POST":
        preg_num = request.POST.get("preg_num")
        glu_con = request.POST.get("glu_con")
        blood_pre = request.POST.get("blood_pre")
        thickness = request.POST.get("thickness")
        insulin = request.POST.get("insulin")
        bmi = request.POST.get("bmi")
        age = request.POST.get("age")
        print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(preg_num,glu_con,blood_pre,thickness,insulin,bmi,age))
        return render(request,"base.html",context)
    return render(request,"home.html",context)