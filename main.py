#!/usr/bin/env python3
import json,os,sys,urllib.request,urllib.error
E=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no")
V={"p":1,"n":3,"b":3,"r":5,"q":9,"k":200};MV=V
def P(p,b):
 r=urllib.request.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(r) as x:return json.load(x)
 except urllib.error.HTTPError as e:sys.exit(str(e.code))
def bo(f):
 d={};i=0
 for row in f.split()[0].split("/"):
  j=0
  for c in row:
   if c.isdigit():j+=int(c)
   else:d[chr(97+j)+str(8-i)]=c;j+=1
  i+=1
 return d
def sq(s):return(ord(s[0])-97,int(s[1])-1)
def us(x,y):return chr(97+x)+str(y+1)
def ib(x,y):return 0<=x<8 and 0<=y<8
def gen(f,s):
 d=bo(f);m=[]
 for k,p in d.items():
  if s=="w" and not p.isupper():continue
  if s=="b" and not p.islower():continue
  x,y=sq(k);pc=p.lower()
  if pc=="p":
   dd=1 if p.isupper() else -1;st=6 if p.isupper() else 1;nx,ny=x,y+dd
   if ib(nx,ny) and us(nx,ny) not in d:
    if ny==0 or ny==7:
     for pr in"qrbn":m.append(k+us(nx,ny)+pr)
    else:m.append(k+us(nx,ny))
    if y==st:
     nx2,ny2=x,y+2*dd
     if ib(nx2,ny2) and us(nx2,ny2) not in d:m.append(k+us(nx2,ny2))
   for dx in(-1,1):
    nx,ny=x+dx,y+dd
    if not ib(nx,ny):continue
    t=us(nx,ny)
    if t in d and(d[t].isupper()!=p.isupper()):m.append(k+t)
    # simple: allow ep not handled, rare
  elif pc=="n":
   for dx,dy in[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]:
    nx,ny=x+dx,y+dy
    if not ib(nx,ny):continue
    t=us(nx,ny)
    if t not in d or(d[t].isupper()!=p.isupper()):m.append(k+t)
  elif pc=="k":
   for dx in(-1,0,1):
    for dy in(-1,0,1):
     if dx==0 and dy==0:continue
     nx,ny=x+dx,y+dy
     if not ib(nx,ny):continue
     t=us(nx,ny)
     if t not in d or(d[t].isupper()!=p.isupper()):m.append(k+t)
  else:
   dr=[]
   if pc=="b" or pc=="q":dr+=[(1,1),(1,-1),(-1,1),(-1,-1)]
   if pc=="r" or pc=="q":dr+=[(1,0),(-1,0),(0,1),(0,-1)]
   for dx,dy in dr:
    nx,ny=x+dx,y+dy
    while ib(nx,ny):
     t=us(nx,ny)
     if t in d:
      if d[t].isupper()!=p.isupper():m.append(k+t)
      break
     m.append(k+t);nx+=dx;ny+=dy
 return m
def ev(f):
 d=bo(f);s=0
 for p in d.values():v=V[p.lower()];s+=v if p.isupper() else -v
 return s
def mvf(f,m):
 d=bo(f);x=d.copy();fr,to=m[0:2],m[2:4];p=x.get(fr)
 if not p:return f
 del x[fr]
 if len(m)==5:
  pr=m[4]
  if p.isupper():p={'q':'Q','r':'R','b':'B','n':'N'}.get(pr,pr.upper())
  else:p={'q':'q','r':'r','b':'b','n':'n'}.get(pr,pr.lower())
 x[to]=p
 rs=[];i=0
 while i<8:
  row="";e=0;j=0
  while j<8:
   sqn=us(j,7-i)
   if sqn in x:
    if e:row+=str(e);e=0
    row+=x[sqn]
   else:e+=1
   j+=1
  if e:row+=str(e)
  rs.append(row);i+=1
 sd="b" if f.split()[1]=="w" else "w"
 return "/".join(rs)+" "+sd+" - - 0 1"
def ordm(ms,f):
 d=bo(f)
 def sc(m):
  p=d.get(m[0:2],"P").lower();t=d.get(m[2:4]);cap=V[t.lower()] if t else 0;pr=V.get(m[4].lower(),0) if len(m)==5 else 0
  return-(cap*4+pr)+MV.get(p,0)
 return sorted(ms,key=sc)
def sr(f,dp,s,a,b):
 if dp<=0:return None,ev(f)
 ms=gen(f,s);ms=ordm(ms,f)
 if not ms:return None,ev(f)
 if s=="w":
  bm=None
  for m in ms[:14]:
   nf=mvf(f,m);_,v=sr(nf,dp-1,"b",a,b)
   if v>a:a=v;bm=m
   if a>=b:break
  return bm,a
 else:
  bm=None
  for m in ms[:14]:
   nf=mvf(f,m);_,v=sr(nf,dp-1,"w",a,b)
   if v<b:b=v;bm=m
   if b<=a:break
  return bm,b
while True:
 g=P("/game",{})
 if g.get("status")=="done":break
 while g.get("status")=="your_move":
  lm=g.get("legal_moves") or [];fen=g["fen"];sd="w" if fen.split()[1]=="w" else "b"
  mv=None
  if lm:
   mv,_=sr(fen,2,sd,-10**9,10**9)
   if mv not in lm:mv=lm[0]
  g=P("/move",{"game":g["game"],"move":mv or lm[0]})
  if not lm:break
 print("g",file=sys.stderr)
print("done",file=sys.stderr)
