import React from "react";
import { HashRouter as Router, Switch, Route } from 'react-router-dom';
import Login from './Components/Auth/Login';
import Register from './Components/Auth/Register';
import Professor from "./Components/Professor";
import Student from "./Components/Student";
import Classes from "./Components/Classes";


function App() {
  return (
    <Router>
      <div className="container">
        <Switch>
          <Route path="/profile/professor/:id" component={Professor} />
          <Route path="/profile/student/:id" component={Student} />
          <Route path="/register/" component={Register} />
          <Route path="/classes/" component={Classes} />
          <Route exact path="/" component={Login} />
        </Switch>
      </div>
    </Router>
    
  );
}

export default App;