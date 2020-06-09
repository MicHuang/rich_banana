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
        <div className="row item-container">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Price</th>
              </tr>
            </thead>
            <tbody>
              {Object.keys(allFish).map((key) => (
                <tr key={key}>
                  <th scope="row"><img className="card-img-top" src={allFish[key]["icon_uri"]} /></th>
                  <td>{allFish[key].name["name-EUen"]}</td>
                  <td>${allFish[key].price}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    }
  }
}

export default Fish;
