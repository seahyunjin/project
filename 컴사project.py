from tkinter import * # Import tkinter
from PIL import ImageTk
import math
import webbrowser
import tkinter as tk
import os
from collections import Counter
from tkinter import messagebox

class WidgetsDemo:
    def __init__(self):
        window = Tk() 
        window.title("epl 경기시간 프로그램") 
        window.geometry("700x500")
        window.configure(bg="steelblue")
        
        label = Label(window)
        img = PhotoImage(file = "C:/Users/seahe/Desktop/pythonproject/epl2.png", master = window)
        img.subsample(15)
        label.config(image = img)
        label.pack()


        frame1 = Frame(window) 
        frame1.pack()
        label = Label(frame1, text = "경기날짜를 입력해주세요: ",bg="deepskyblue")
     
        self.name = IntVar()
        entryName = Entry(frame1, textvariable = self.name,bg="aqua") 
        btGetName = Button(frame1, text = "경기 시작시간 가져오기", command = self.processButton,bg='skyblue')
        message = Message(frame1, text = "경기 날짜를 가져올 때는 년,월,일 순서로 써주세요",bg="deepskyblue")
        aName = Button(frame1,text= "중계 채널로 이동하기", command = self.sports1,fg='red',bg='skyblue')
        bName = Button(frame1,text= "EPL 순위 확인하기", command = self.sports2,fg='red',bg='skyblue')
        aName.grid(row = 3, column = 1)
        bName.grid(row = 3, column = 2)
        label.grid(row = 1, column = 1)
  
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        
        # Add a text
        text = Text(window) 
        text.pack()
        text.insert(END, "경기 날짜를 가져올 때는 년,월,일 순서로 써주세요!! ")
        text.insert(END, "Ex) 2020년 10월 16일 경기이면 20201016로 입력해주세요. ")
        text.insert(END, "이 프로그램의 경기 시간은 epl 프리미어리그 2020~2021 경기 시간입니다 그외에 다른 년도 경기 시간을 불러올 수 없습니다.")
        text.insert(END, "                                                                                                  ")
        text.insert(END, "하늘색 버튼을 누르면 실시간 경기를 보거나 EPL 순위를 확인 할 수 있습니다.")
        
        window.mainloop() 
    
    def processButton(self):
        if self.name.get()==20201016:
            msg = messagebox.showinfo("경기시간","오늘은 경기가 있습니다!!" )
        elif self.name.get()==20201124:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 2시 30분에 번리 VS 펠리스, 새벽 5시에 울버햄튼 VS 사우샘스턴 경기가 있습니다." )
        elif self.name.get()==20201128:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 5시에 펠리스 VS 뉴캐슬, 저녁 9시 30분에 브라이튼 VS 리버풀 경기가 있습니다." )
        elif self.name.get()==20201129:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 맨시티 VS 번리, 새벽 2시 30분에 에버튼 VS 리즈, 새벽 5시에 웨스트브롬 VS 셰필드, 저녁 11시에 사우샘프턴 VS 맨유 경기가 있습니다." )
        elif self.name.get()==20201130:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시 30분에 첼시 VS 토트넘, 새벽 4시 15분에 아스널 VS 울버햄튼 경기가 있습니다." )
        elif self.name.get()==20201201:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 2시 30분에 레스터 VS 풀럼, 새벽 5시에 웨스트햄 VS 아스톤 빌라 경기가 있습니다." )
        elif self.name.get()==20201205:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 아스톤 빌라 VS 뉴캐슬, 저녁 9시 30분에 번리 VS 에버턴 경기가 있습니다." )
        elif self.name.get()==20201206:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 맨시티 VS 풀럼, 새벽 2시 30분에 웨스트햄 VS 맨유, 새벽 5시에 첼시 VS 리즈, 저녁 11시에 웨스트브롬 VS 팰리스, 저녁 11시 15분에 셰필드 VS 레스터 경기가 있습니다." )
        elif self.name.get()==20201207:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시 30분에 아스널 VS 토트넘, 새벽 4시 15분에 리버풀 VS 울버햄튼 경기가 있습니다." )
        elif self.name.get()==20201208:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 5시에 브라이튼 VS 사우샘프턴 경기가 있습니다." )
        elif self.name.get()==20201213:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 리즈 VS 웨스스햄, 팰리스 VS 토트넘, 에버턴 VS 첼시, 풀럼 VS 리버풀 경기가 있습니다." )
        elif self.name.get()==20201214:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 레스터 VS 브라이튼, 아스널 VS 번리 경기가 있습니다." )
        elif self.name.get()==20201216:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 4시 45분에 아스널 VS 사우샘프턴, 아스톤 빌라 VS 번리, 리즈 VS 뉴캐슬, 울버햄튼 VS 첼시 경기가 있습니다." )
        elif self.name.get()==20201217:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 5시에 맨시티 VS 웨스트브롬, 리버풀 VS 토트넘 경기가 있습니다." )
        elif self.name.get()==20201220:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 사우샘프턴 VS 맨시티, 레스터 VS 토트넘, 웨스트브롬 VS 아스톤빌라, 번리 VS 울버햄튼, 첼시 VS 웨스트햄, 펠리스 VS 리버풀, 맨유 VS 리즈, 뉴캐슬 VS 풀럼, 에버턴 VS 아스널, 브라이튼 VS 셰필드 경기가 있습니다." )
        elif self.name.get()==20201227:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 아스널 VS 첼시, 풀럼 VS 사우샘프턴, 리버풀 VS 웨스트브롬, 아스톤 빌라 VS 펠리스, 리즈 VS 번리, 맨시티 VS 뉴캐슬, 셰필드 VS 에버턴, 울버햄튼 VS 토트넘, 레스터 VS 맨유, 웨스트햄 VS 브라이튼 경기가 있습니다." )
        elif self.name.get()==20201229:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 웨스트브롬 VS 리즈, 풀럼 VS 토트넘, 사우샘프턴 VS 웨스트햄, 맨유 VS 울버햄튼, 뉴캐슬 VS 리버풀, 에버턴 VS 맨시티, 브라이튼 VS 아스널, 번리 VS 셰필드, 팰리스 VS 레스터, 첼시 VS 아스톤 빌라 경기가 있습니다." )
        elif self.name.get()==20210103:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 번리 VS 풀럼, 뉴캐슬 VS 레스터, 맨유 VS 아스톤 빌라, 첼시 vS 맨시티, 애버턴 VS 웨스트햄, 웨스트브롬 VS 아스널, 사우샘프턴 VS 리버풀, 브라이튼 VS 울버햄튼, 토트넘 VS 리즈, 팰리스 VS 셰필드")
        elif self.name.get()==20210113:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 4시 45분에 아스톤빌라 VS 토트넘, 풀럼 VS 맨유, 리즈 VS 사우샘프턴, 아스널 VS 팰리스, 울버햄튼 VS 에버턴, 웨스트헴 VS 웨스트브롬, 셰필드 VS 뉴캐슬, 레스터 VS 첼시 경기가 있습니다." )
        elif self.name.get()==20210114:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 5시에 리버풀 VS 번리, 맨시티 VS 브라이튼 경기가 있습니다." )
        elif self.name.get()==20210117:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 리버풀 VS 맨유, 아스널 VS 뉴캐슬, 아스톤 빌라 VS 에버턴, 리즈 VS 브라이튼, 레스터 VS 사우샘프턴, 풀럼 VS 첼시, 맨시티 VS 팰리스, 웨스트햄 VS 번리, 울버햄튼 VS 웨스트브롬, 셰필드 VS 토트넘 경기가 있습니다." )
        elif self.name.get()==20210127:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 4시 45분에 번리 VS 아스톤빌라, 풀럼 VS 브라이튼, 에버턴 VS 레스터, 새벽 5시에는 맨유 VS 셰필드, 웨스트브롬 VS 맨시티 경기가 있습니다." )
        elif self.name.get()==20210127:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 4시 45분에 뉴캐슬 VS 리즈, 토트넘 VS 리버풀, 사우샘프턴 VS 아스널, 첼시 VS 울버햄튼 새벽 5시에는 팰리스 VS 웨스트햄 경기가 있습니다." )
        elif self.name.get()==20210131:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 웨스트브롬 VS 풀럼, 맨시티 VS 셰필드, 에버턴 VS 뉴캐슬, 레스터 VS 리즈, 팰리스 VS 울버햄튼, 웨스트햄 VS 리버풀, 사우샘프턴 VS 아스톤빌라, 첼시 VS 번리, 아스널 VS 맨유, 토트넘 VS 브라이튼 경기가 있습니다." )
        elif self.name.get()==20210203:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 4시 45분에 셰필드 VS 웨스트 브롬, 아스톤빌라 VS 웨스트햄, 울버햄튼 VS 아스널, 풀럼 VS 레스터, 리즈 VS 에버턴, 번리 VS 맨시티 새벽 5시에는 맨유 VS 사우샘프턴 경기가 있습니다." )
        elif self.name.get()==20210204:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 4시 45분에 토트넘 VS 첼시, 뉴캐슬 VS 팰리스 새벽 5시에는 리버풀 VS 브라이튼 경기가 있습니다." )
        elif self.name.get()==20210207:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 웨스트햄 VS 풀럼, 번리 VS 브라이튼, 아스톤빌라 VS 아스널, 리버풀 VS 맨시티, 레스터 VS 울버햄튼, 리즈 VS 펠리스, 셰필드 VS 첼시, 토트넘 VS 웨스트브롬, 맨유 VS 애버턴, 뉴캐슬 VS 사우샘프턴 경기가 있습니다." )
        elif self.name.get()==20210214:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 에버턴 VS 풀럼, 맨시티 VS 토트넘, 브라이튼 VS 아스톤빌라, 웨스트햄 VS 셰필드, 아스널 VS 리즈, 웨스트브롬 VS 맨유, 사우샘프턴 VS 울버햄튼, 첼시 VS 뉴캐슬, 레스터 VS 리버풀, 팰리스 VS 번리 경기가 있습니다." )
        elif self.name.get()==20210221:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 아스널 VS 맨시티, 번리 VS 웨스트브롬, 웨스트햄 VS 토트넘, 맨유 VS 뉴캐슬, 사우샘프턴 VS 첼시, 아스톤빌라 VS 레스터, 풀럼 VS 셰필드, 브라이튼 VS 팰리스, 리버풀 VS 에버턴, 울버햄튼 VS 리즈 경기가 있습니다." )
        elif self.name.get()==20210228:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 뉴캐슬 VS 울버햄튼, 리버풀 VS 셰필드, 웨스트브롬 VS 브라이튼, 토트넘 VS 번리, 맨시티 VS 웨스트햄, 팰리스 VS 풀럼, 리즈 VS 아스톤빌라, 에버턴 VS 사우샘프턴, 아스널 VS 레스터, 첼시 VS 맨유 경기가 있습니다." )
        elif self.name.get()==20210307:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 첼시 VS 에버턴, 사우샘프턴 VS 셰필드, 번리 VS 아스널, 리버풀 VS 풀럼, 맨시티 VS 맨유, 브라이튼 VS 레스터, 울버햄튼 VS 아스톤빌라, 웨스트햄 VS 리즈, 토트넘 VS 펠리스, 웨스트브롬 VS 뉴캐슬 경기가 있습니다." )
        elif self.name.get()==20210314:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 아스널 VS 토트넘, 뉴캐슬 VS 아스톤빌라, 맨유 VS 웨스트햄, 울버햄튼 VS 리버풀, 풀럼 VS 맨시티, 에버턴 VS 번리, 레스터 VS 셰필드, 리즈 VS 첼시, 사우샘프턴 VS 브라이튼, 펠리스 VS 웨스트브롬 경기가 있습니다." )
        elif self.name.get()==20210321:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 1시에 풀럼 VS 리즈, 번리 VS 레스터, 셰필드 VS 아스톤빌라, 브라이튼 VS 뉴캐슬, 팰리스 VS 맨유, 웨스트브롬 VS 에버턴, 토트넘 VS 사우샘프턴, 맨시티 VS 울버햄튼, 웨스트햄 VS 아스널, 첼시 VS 리버풀 경기가 있습니다." )
        elif self.name.get()==20210404:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 뉴캐슬 VS 토트넘, 울버햄튼 VS 웨스트햄, 레스터 VS 맨시티, 브라이튼 VS 맨유, 아스널 VS 리버풀, 아스톤 빌라 VS 풀럼, 에버턴 VS 팰리스, 사우샘프턴 VS 번리, 리즈 VS 셰필드, 첼시 VS 웨스트브롬 경기가 있습니다." )      
        elif self.name.get()==20210411:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 셰필드 VS 아스널, 리버풀 VS 아스톤 빌라, 풀럼 VS 울버햄튼, 웨스트브롬 VS 사우샘프턴, 토트넘 VS 맨유, 번리 VS 뉴캐슬, 웨스트햄 VS 레스터, 맨시티 VS 리즈, 브라이튼 VS 에버턴, 펠리스 VS 첼시 경기가 있습니다." )      
        elif self.name.get()==20210418:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 레스터 VS 웨스트브롬, 뉴캐슬 VS 웨스트햄, 아스톤 빌라 VS 맨시티, 리즈 VS 리버풀, 맨유 VS 번리, 에버턴 VS 토트넘, 울버햄튼 VS 셰필드, 아스널 VS 풀럼, 사우샘프턴 VS 펠리스, 첼시 VS 브라이튼 경기가 있습니다." )      
        elif self.name.get()==20210425:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 리즈 VS 맨유, 아스널 VS 에버턴, 아스톤 빌라 VS 웨스트브롬, 리버풀 VS 뉴캐슬, 울버햄튼 VS 번리, 레스터 VS 펠리스, 웨스트햄 VS 첼시, 셰필드 VS 브라이튼, 맨시티 VS 샤우샘프턴, 풀럼 VS 토트넘 경기가 있습니다." )      
        elif self.name.get()==20210502:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 맨유 VS 리버풀, 첼시 VS 풀럼, 브라이튼 VS 리즈, 사우샘프턴 VS 레스터, 뉴캐슬 VS 아스널, 에버턴 VS 아스톤 빌라, 토트넘 VS 셰필드, 번리 VS 웨스트햄, 팰리스 VS 맨시티, 웨스트브롬 VS 울버햄튼 경기가 있습니다." )      
        elif self.name.get()==20210509:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 웨스트햄 VS 에버턴, 셰필드 VS 팰리스, 레스터 VS 뉴캐슬, 리즈 VS 토트넘, 울버햄튼 VS 브라이튼, 맨시티 VS 첼시, 아스톤 빌라 VS 맨유, 풀럼 VS 번리, 아스널 VS 웨스트브롬, 리버풀 VS 사우샘프턴 경기가 있습니다." )      
        elif self.name.get()==20210512:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 3시 45분에 번리 VS 리즈, 브라이튼 VS 웨스트햄, 에버턴 VS 셰필드, 새벽 4시에 맨유 VS 레스터, 웨스트브롬 VS 리버풀 경기가 있습니다. ")
        elif self.name.get()==20210513:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 3시 45분에 토트넘 VS 울버햄튼, 사우샘프턴 VS 풀럼, 뉴캐슬 VS 맨시티, 첼시 VS 아스널 새벽 4시에 팰리스 VS 아스톤 빌라 경기가 있습니다. ")
        elif self.name.get()==20210516:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 첼시 VS 레스터, 웨스트브롬 VS 웨스트햄, 사우샘프턴 VS 리즈, 브라이튼 VS 맨시티, 뉴캐슬 VS 셰필드, 맨유 VS 풀럼, 팰리스 VS 아스널, 토트넘 VS 아스톤 빌라, 에버턴 VS 울버햄튼, 번리 VS 리버풀 경기가 있습니다." )      
        elif self.name.get()==20210524:
            msg = messagebox.showinfo("경기시간","오늘은 새벽 12시에 울버햄튼 VS 맨유, 웨스트햄 VS 사우샘프턴, 셰필드 VS 번리, 리버풀 VS 팰리스, 레스터 VS 토트넘, 아스톤 빌라 VS 첼시, 맨시티 VS 에버턴, 리즈 VS 웨스트브롬, 풀럼 VS 뉴캐슬, 아스널 VS 브라이튼 경기가 있습니다." )      
        else:
            msg = messagebox.showinfo("경기시간","오늘은 경기가 없습니다!!" )
            
    def sports1(self):
        webbrowser.open("https://www.spotvnow.co.kr/intro")
    def sports2(self):
        webbrowser.open("https://www.premierleague.com/tables")


WidgetsDemo()

