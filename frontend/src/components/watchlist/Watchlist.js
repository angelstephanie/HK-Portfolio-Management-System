import React, { useEffect, useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import WatchlistItem from './WatchlistItem';

const Watchlist = () => {
    const endpoint = `http://127.0.0.1:5000`;
    const [watchListItems, setWatchListItems] = useState([]);

    useEffect(() => {
        fetch(`${endpoint}/watchlist`)
        .then(response => response.json())
        .then(data => {
            // Handle the fetched watchlist data if needed
            setWatchListItems(data);
        })
        .catch(error => {
            console.error('Error fetching watchlist:', error);
        });
    }, []);

    return (
        <Container fluid >
            <Row>
                {watchListItems.map((item, index) => (<div
                    key={index}
                    style={{
                        borderBottom: index !== watchListItems.length - 1 ? '1px solid #e0e0e0' : 'none'
                    }}
                >
                    <WatchlistItem item={item} />
                </div>
                ))}
            </Row>
        </Container>
    );
};

export default Watchlist;