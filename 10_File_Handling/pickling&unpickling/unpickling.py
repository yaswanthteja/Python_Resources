import pickle

f1=open('data.pkl','rb')

while True:
    try:
        obj=pickle.load(f1)
        print(obj)
        obj.display()
    except EOFError:
        print('All the data picklied')
        break
f1.close()

