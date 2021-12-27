import React, { PureComponent, useState } from 'react';
import { NavLink } from 'react-router-dom';


class Navbar extends React.Component {
    
    render() { 
        return (
            <div className="topnav">
                <NavLink to="/">Home</NavLink>
                <NavLink to="/login">Login</NavLink>
                <NavLink to="/register">Register</NavLink>
                <NavLink to="/chat">Chat</NavLink>
            </div>);
    }

    
}



export default Navbar;