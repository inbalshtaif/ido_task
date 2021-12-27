import React, { PureComponent, useState } from 'react';
import SendMessageForm from './sendMessageForm';
import MessagesList from './messagesList';
import io from "socket.io-client";


class Chat extends React.Component {
    state={
        message: "",
        users:[],
        roomId: "",
        chat: [],
        socketConnection: io.connect('http://localhost:8080', { transports: ['websocket', 'polling', 'flashsocket'] }),
    }

    // function sleep(ms){
    //     return new Promise(resolve => setTimeout(resolve, ms));
    // }

    

    handleSubmit = async (event) => {
        await this.createRoomId(event);
        console.log(this.state.roomId);
        await this.joinRoom();
        const myTimeout = setTimeout(this.fetchChat, 1000);
        
    }

    createRoomId = async (anotherUser) =>{
        let userId = parseInt(this.props.userId);
        let anotherUserId = parseInt(anotherUser);
        if (userId < anotherUser){
            this.setState({"roomId": this.props.userId + '&' + anotherUserId});
        }
        else{
            this.setState({"roomId": anotherUserId + '&' + this.props.userId});
        }
    }

    render() { 
        return <div className="chat">
                    <h3>{this.state.message}</h3>
                    <div className="users">
                
                        {this.state.users.map((user) => 
                            (<button onClick={() => {this.handleSubmit(user.id)}}>{user.first_name}</button>))}
                    </div>
                    <div className="MessagesList">
                        <MessagesList roomId={this.state.roomId} chat={this.state.chat} users={this.state.users} loggedUser={this.props.userName}  />
                    </div>
                    <div className="textBoxArea">
                        <SendMessageForm url={this.props.url} roomId={this.state.roomId} userId={this.props.userId} chat={this.state.chat} addMessageToChat={this.addMessageToChat} />
                    </div>
               </div>;
    }

    componentDidMount  =  async() => {
        //This method will work when the component will mount
        await this.fetchUsers();
        await this.fetchMessage();
    }


    fetchUsers = async () =>{

        let res = await fetch('http://localhost:8080/get_Users');
        res = await res.json();
        this.setState({users:res});
        await this.checkIfLogged();

        if (this.state.message == "Enjoy talking to other users"){
            const newList = this.state.users.filter((user) => user.first_name !== this.props.userName);
            this.setState({users:newList}); 
        }
    }

    checkIfLogged = async () =>{
        const loggedUser = this.props.userName;
        if (loggedUser == "stranger"){
            await this.setState({['message']: "Make sure you log in or register first"});
        }
        else {
            await this.setState({['message']: "Enjoy talking to other users"});
        }
    }


    joinRoom = async () => {

        const messageIO ={"room_id": this.state.roomId}
        await console.log(this.state.socketConnection.emit('join', JSON.stringify(messageIO)));
        console.log(this.state.chat)
    }

    fetchChat = async () => {

        let res = await fetch('http://localhost:8080/get_Chat/' + this.state.roomId);
        let data = await res.json();
        await this.setState({"chat": data});
        console.log(this.state.chat);
    }

    
    fetchMessage = async () => {
        await this.state.socketConnection.on("chat", async (data) => {
            console.log(data)
            this.addMessageToChat(data);
            //await this.addMessageToChat(data);
            console.log("hello");
            console.log(this.state.chat);
        });
    }

    addMessageToChat = async (message) => {
        let updatedChat = this.state.chat;
        console.log(updatedChat)
        console.log(message)
        await updatedChat.push(message);
        await this.setState({"chat": updatedChat});
        console.log(this.state.chat);
    }
}

export default Chat;