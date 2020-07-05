import React, { Component } from 'react';

class Fish extends Component {
  constructor(props){
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount(){
    fetch('http://acnhapi.com/v1/fish')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result
          })
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          })
        }
      );
  }

  render(){
    const { error, isLoaded, items } = this.state;
    if(error){
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded){
      return <div>Loading...</div>;
    } else {
      return(
        <div name="fish" onClick={this.props.changeItem.bind(this, items)} style={{cursor: "pointer"}}>Fish</div>
      );
    }
  }
}

export default Fish;
