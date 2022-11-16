import React, { useState } from "react";
// this context allows variables to be passed between many pages. The Loggedin state as one important one
const AuthContext = React.createContext({
  token: "",
  isLoggedIn: false,
  login: (token) => {},
  logout: () => {},
  username: "",
  getUser: (username) => {},
});

// local storage controls the token that allows the user to stay logged in
const storageToken = localStorage.getItem("token");

export const AuthContextProvider = (props) => {
  const [token, setToken] = useState(storageToken);
  const [username, setUsername] = useState("");
  const [userId, setUserId] = useState("");

  const userIsLoggedIn = !!token;

  const loginHandler = (token) => {
    setToken(token);
    setUsername(username);
    localStorage.setItem("token", token);
  };

  const logoutHandler = () => {
    setToken(null);
    setUsername("");
    localStorage.removeItem("token", token);
  };

  const getUserHandler = (user) => {
    setUsername(user);
  };

  const getUserIDHandler = (user) => {
    setUserId(user);
  };

  const contextValue = {
    token: token,
    isLoggedIn: userIsLoggedIn,
    login: loginHandler,
    logout: logoutHandler,
    username: username,
    getUser: getUserHandler,
    getUserId: getUserIDHandler,
    userId: userId,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
