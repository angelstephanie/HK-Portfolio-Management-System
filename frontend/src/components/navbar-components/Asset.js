import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const Asset = () => {
    const {symbol} = useParams();

    return (
        <div className="asset">
            <h1>{symbol}</h1>
        </div>
    );
}

export default Asset;