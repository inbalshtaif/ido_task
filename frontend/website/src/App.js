import Navbar from './components/Navbar.jsx'
import './App.css';
import Books from './components/Books';
import Chat from './components/chat';
import Login from './components/login.jsx';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React, { useState } from 'react';
import Register from './components/register.jsx';


function App() {
  const [userName, setUserName] = useState("stranger");
  const [userId, setUserId] = useState();

  const handleUserName = async (userName, userid) => {
    localStorage.setItem('user', userName)
    setUserName(localStorage.getItem('user'))
    setUserId(userid)
  }

  const url = "http://localhost:3000/";


  return (
    <BrowserRouter>
        <div className="App">
          <h1>Book Recommendations </h1>
          <h2>Hello {userName}</h2>
          <Navbar url={url} />
            <Routes>
             <Route path="/" element={ <Books url={url} />}></Route>
             <Route path="/login" element={ <Login url={url} handleUserName={handleUserName} />}></Route>
             <Route path="/register" element={ <Register url={url} handleUserName={handleUserName} />}></Route>
             <Route path="/chat" element={ <Chat url={url} userName={userName} userId={userId} />}></Route>
           </Routes>
        </div> 
      </BrowserRouter>

  );
}



export default App;