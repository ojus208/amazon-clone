import React, { useState, useEffect } from 'react';
import './css_file/carsousel.css'
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';
import Main_body from './main_body'


function Carousel_amazon() {

const [trending, settrending] = useState([])

useEffect(() => {
    
const fetching =  async ()=>{
    const Response = await fetch('http://127.0.0.1:8000/api/trending/')
    const response_json = await Response.json();
    console.log(response_json)
    settrending(response_json)

}

fetching();

}, [])



if (trending === undefined){
    return(
        <div className="loading">
            loading
        </div>
    )
}
else{
    return (
        <div className="body">
            <Carousel infiniteLoop={true} autoPlay={true}>
                {
                trending.map(trend=>(
                    <div className="car" key={trend.id} >
                        <img src={`http://127.0.0.1:8000${trend.poster}`} alt={trend.id} />
                        <div className="blur"></div>
                    </div>
                ))}
            </Carousel>
        </div>
    )}
}


export default Carousel_amazon;