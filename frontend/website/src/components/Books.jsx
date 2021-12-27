import React, { PureComponent, useState } from 'react';

class Books extends React.Component {
    state={
        users:[]
    }
    render() { 
        return <div>{this.state.users.map((user) => (<h3>{"Book: " + user.Book_name + " -> Name: " + user.first_name}</h3>))}</div>;
    }

    componentDidMount  =  async() => {
        //This method will work when the component will mount
        await this.fetchUsers()
    }

    fetchUsers = async () =>{

        let res = await fetch('http://localhost:8080/get_Users');
        res = await res.json();
        this.setState({users:res});
    }

}
 
export default Books;