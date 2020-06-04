import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/header';
import Dashboard from './acnh-items/dashboard';

class App extends Component{
  render(){
    return(
      <Fragment>
        <Header />
        <Dashboard />
      </Fragment>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
