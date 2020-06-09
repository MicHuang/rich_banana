import React, { useState, Fragment} from 'react';
import Fish from './Fish';
import Bugs from './Bugs';


export default function Dashboard() {

  const [itemInfo, setItemInfo] = useState([]);
  const [whichItem, setWhichItem] = useState('fish')

  const changItem = (items) => {
    setItemInfo(items)
  }

  const onClick = (e) => {
    const itemName = e.target.getAttribute("name");
    const preItem = document.getElementById(whichItem)
    if (preItem !== null){
      preItem.classList.remove("active");
    } 
    setWhichItem(itemName);
    document.getElementById(itemName).classList.add("active");
  }

  return (
    <Fragment>
      <div className="tab-container">
        <ul className="nav nav-tabs">
          <li className="nav-item">
              <div className="nav-link" onClick={onClick} id="fish">
                <Fish changeItem={changItem}/>
              </div>            
          </li>
          <li className="nav-item" >
          <div className="nav-link" onClick={onClick} id="bugs">
                <Bugs changeItem={changItem}/>
              </div>    
          </li>
        </ul>
      </div>
      
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
              {Object.keys(itemInfo).map((key) => (
                <tr key={key}>
                  <th scope="row"><img src={itemInfo[key]["icon_uri"]} /></th>
                  <td>{itemInfo[key].name["name-EUen"]}</td>
                  <td>${itemInfo[key].price}</td>
                </tr>
              ))}
              
            </tbody>
          </table>
        </div>

    </Fragment>
  )
}
