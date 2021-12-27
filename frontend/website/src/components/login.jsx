import React, { PureComponent, useState, setState } from 'react';

class Login extends React.Component {

  state={
    email:"",
    password:"",
    userName: "",
    userId: ""
  }
   
  
  handleChange = async (evt) => {
    const value = evt.target.value;
    const name = evt.target.name;
   
    await this.setState({[name]: value});
  
}
  
  handleSubmit = async (event) => {
    let dic = {"e-mail": this.state.email, "password": this.state.password}
    
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dic)
    };

    let response = await fetch('http://localhost:8080/login', requestOptions);
    let data = await response.json();

    if(data["message"]["message"] == 'Logged successfully'){
      await this.setState({['userName']: data["message"]["userName"]});
      await this.setState({['userId']: data["message"]["userId"]});
      await this.props.handleUserName(this.state.userName, this.state.userId);
    }

    alert(data["message"]["message"])
    event.preventDefault();
  }


    render() { 
        return (
        <div className="login">
        <label>Email:
        <input 
          type="text" 
          name="email"
          onChange={(event) =>this.handleChange(event)}
        />
        </label>
        <label>Password:                
          <input 
            type="text" 
            name="password"
            onChange={(event) => this.handleChange(event)}
          />
        </label>
        <button onClick= {(event) =>this.handleSubmit(event)}>submit</button>
        </div>)
    }

    }
 
export default Login;