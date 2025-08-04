import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import assets from '../../assets/watchlist.json';
import WatchlistItem from './WatchlistItem';

const Watchlist = () => {

    return (
        <Container fluid className="border border-secondary rounded">
            <Row>
                {assets.map((item, index) => (
                            <WatchlistItem item={item} key={item.symbol} />
                ))}
            </Row>
        </Container>
    );
};

export default Watchlist;