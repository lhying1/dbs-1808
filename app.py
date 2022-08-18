#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,request,render_template


# In[4]:


app = Flask(__name__)


# In[5]:


import joblib


# Decorator -> something you have to do before using the function

# In[6]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", r1="temp",r2="temp"))
    else:
        return(render_template("index.html", r1="waiting",r2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




