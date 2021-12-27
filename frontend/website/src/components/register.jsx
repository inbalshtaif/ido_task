import React, { PureComponent, useState, setState } from 'react';

class Register extends React.Component {

  state={
    first_name: "",
    last_name: "", 
    id: "",
    email: "", 
    Book_name: "",
    password: ""
  }
   
  
  handleChange = async (evt) => {
    const value = evt.target.value;
    const name = evt.target.name;

    await this.setState({[name]: value});
  
}
  
  handleSubmit = async (event) => {
    let dic = {"first_name": this.state.first_name, 
               "last_name": this.state.last_name, 
               "id": this.state.id, 
               "e-mail": this.state.email, 
               "Book_name": this.state.Book_name, 
               "password": this.state.first_name}
    
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dic)
    };

    let response = await fetch('http://localhost:8080/add_User', requestOptions);
    let data = await response.json();
    await this.props.handleUserName(this.state.first_name);
    alert(data["message"]["message"]);
    event.preventDefault();
  }


    render() { 
        return (
        <div className="register">
        <label>First Name:
        <input 
          type="text" 
          name="first_name"
          onChange={(event) =>this.handleChange(event)}/>
        </label>
        <label>Last Name:
        <input 
          type="text" 
          name="last_name"
          onChange={(event) =>this.handleChange(event)}/>
        </label>
        <label>Id:
        <input 
          type="text" 
          name="id"
          onChange={(event) =>this.handleChange(event)}/>
        </label>
        <label>Email:
        <input 
          type="text" 
          name="email"
          onChange={(event) =>this.handleChange(event)}/>
        </label>
        <label>Book Name:
        <input 
          type="text" 
          name="Book_name"
          onChange={(event) =>this.handleChange(event)}/>
        </label>
        <label>Password:                
          <input 
            type="text" 
            name="password"
            onChange={(event) => this.handleChange(event)}/>
        </label>
        <button onClick= {(event) =>this.handleSubmit(event)}>submit</button>
        </div>)
    }

    }
 
export default Register;