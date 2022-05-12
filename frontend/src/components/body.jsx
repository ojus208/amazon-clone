import React from 'react';
import Carousel_amazon from './carousel';
import Main_body from './main_body'


function Body() {
    return(
        <div className="body" style={{background : 'whitesmoke'}}>
            <Carousel_amazon />
            <Main_body />
        </div>
    )
}


export default Body;