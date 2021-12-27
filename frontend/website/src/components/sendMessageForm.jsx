import React, { PureComponent, useState } from 'react';
import io from "socket.io-client";

class SendMessageForm extends React.Component {
    state={
        message: 'Please write a message',
        chat: this.props.chat
    }




    handleChange = async (event) => {
        await this.setState({'message': event.target.value});
        console.log(this.state.message);
    }
    
    handleSubmit = async () => {
        await this.sendMessage();
    }

    render() { 
        return <div className="textArea">
                    <label>
                        Text:
                        <textarea onChange={(event) => this.handleChange(event)} />
                        <button onClick={() => {this.handleSubmit()}}>submit</button>
                    </label>
               </div>;
    }

    sendMessage = async () => {

        const socket = io.connect('http://localhost:8080', { transports: ['websocket', 'polling', 'flashsocket'] });
        const messageIO ={"room_id": this.props.roomId, "chat": {'msg': this.state.message, 'date': Date().toLocaleString(), 'who_sent': this.props.userId }};
        await socket.emit("handle_message", JSON.stringify(messageIO));
            
        
    }

    

}
 
export default SendMessageForm;