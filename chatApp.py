from flask import Flask
import csv
import os
server = Flask(__name__)
def chechUserExist(username,password):
  with open('users.csv', "r") as usersExist:
    users=csv.reader(usersExist)
  for user in users:
      if(user[0] == username and user[1] == password):
          return True 
  return False  

@server.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(chechUserExist(username, password)):
          return redirect('lobby')

       
    return render_template('login.html')



@server.route('/lobby', methods = ['POST','GET'])
def lobby():
    if request.method == 'POST':
        rooms = os.listdir('rooms/')
        new_room = request.form['new_room']
        if (str(new_room) + '.txt') in rooms:
            print("exist in:" )
            return "exist"
        else:
            rooms.append(new_room)
            file = open('./rooms/'+ new_room +'.txt', 'w+')
            file.close()
            #return redirect('/chat/' + new_room, room=new_room)
            return render_template('chat.html',room=new_room)  

    return render_template("lobby.html")

#######my:

# @server.route("/lobby", methods=['POST'])
# def lobby():
#     roomName = request.args.get('rname')
#     f = open(str('/rooms/') + str(roomName) + ".txt" ,"w+")
#     f.close()
#     for room in rooms:
#         if room == roomName:
#             return "Room Name already exist!!"
#     rooms.append(roomName)
#     return redirect(url_for('/chat/' + str(roomName), room_names = room))
#     return "you succeed!!"    

@server.route("/chat/<room>")
def chat(room):
    return render_template('chat.html',room=room)
# # Get the room from the parameter
#     room = request.args.get('room')

#     # Check if the room exists
#     if room not in rooms:
#         return render_template('error.html', message="The room does not exist.")

#     # Render the chat room page
#     return render_template('chat.html', room=room)


        #roomName = user = request.args.get('rname')

if __name__ == "__main__":
    server.run(host='0.0.0.0')