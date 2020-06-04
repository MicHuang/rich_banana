import React, { Component } from 'react';

class Fish extends Component {
  constructor(props){
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      allFish: []
    };
  }

  componentDidMount(){
    fetch('http://acnhapi.com/v1/fish')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            allFish: result
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
    const { error, isLoaded, allFish } = this.state;
    if(error){
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded){
      return <div>Loading...</div>;
    } else {
      return(
        <div className="row mt-3" >
        {Object.keys(allFish).map((key) => (
          <div className="card bg-light col-lg-2 col-md-3" key={key}>
            <img className="card-img-top" src={allFish[key]["icon_uri"]} />
            <div className="card-body">
              <h5 className="card-title">{allFish[key].name["name-EUen"]}</h5>
              <h6 className="card-title">{allFish[key].name["name-CNzh"]}</h6>
              <p>${allFish[key].price}</p>
            </div>
          </div>
        ))}
        </div>
          );
    }
  }
}

export default Fish;
