import React, { PureComponent, useState } from 'react';


class Message extends React.Component {
    state={
        whoSent: "",
        message: "",
    }

    

    render() { 
        return <div className="message">
                    <h9>{this.state.whoSent}: {this.state.message}</h9>
               </div>;
    }

    

}
 
export default Message;