#-*- coding: utf-8 -*-
import Tkinter as Tk
import dlweblink as dl
import un7z as un

def dl_from_posting(event=None,text = "None"):
    print text

def dlClicked(event):
    dl_wdw = Tk.Toplevel()
    dl_wdw.geometry("400x400")
    Tk.Label(dl_wdw,text=u"다운로드하고싶은 라디오 포스팅 url을 줄바꿈 단위로 입력하세요").pack()
    text = Tk.Text(dl_wdw)
    text.pack()
    submit_btn = Tk.Button(dl_wdw,text=u"다운로드")
    submit_btn.bind("<Button-1>",dl_from_posting)
    submit_btn.pack()



root = Tk.Tk()
root.title(u"Radibrary Downloader")
root.geometry("400x300")

btn_dl = Tk.Button(text=u"블로그 포스팅 url로 다운로드")
btn_dl.bind("<Button-1>",dlClicked)
btn_dl.pack()

root.mainloop()
