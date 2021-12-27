import React, { PureComponent, useState } from 'react';
import Message from './message';
import SendMessageForm from './sendMessageForm';


class MessagesList extends React.Component {
    state={
        room_id: this.props.roomId,
        chat: this.props.chat,
        users: this.props.users,
    }

    

    findUserName = (userId) => {
        let userName = this.props.loggedUser;
        this.state.users.forEach(user => {
            if(user.id == userId){
                userName = user.first_name;
            }
        });
        return userName;
    }
 
    componentDidMount  =  async() => {
        //This method will work when the component will mount
        console.log(this.props.chat);
        console.log(this.state.users);
    }

    componentDidUpdate = () => {

        if (this.state.chat !== this.props.chat) {
          this.setState({"chat": this.props.chat})
        };

        if (this.state.users !== this.props.users) {
            this.setState({"users": this.props.users})
          };
      }

      showChat = () => {
          if(this.state.chat != []){
            {this.state.chat.map((message) => (<h3>{ this.findUserName(message.who_sent) + " : " + message.msg}</h3>))}
        }
          else{
            <h3>Empty chat</h3>
            }
      }
    


    render() { 
        return <div className="prevchat">
                    {/* {this.showChat} */}
                    {this.state.chat.map((message) => (<h3>{ this.findUserName(message.who_sent) + " : " + message.msg}</h3>))}
                </div>
               
    }

    

}
 
export default MessagesList;