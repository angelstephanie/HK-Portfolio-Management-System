import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import assets from '../../assets/watchlist.json';
import WatchlistItem from './WatchlistItem';

const Watchlist = () => {
    const [watchlist, setWatchlist] = useState(assets); // Initialize with JSON data

    // const handleRemoveItem = (index) => {
    //     const updatedWatchlist = watchlist.filter((_, i) => i !== index);
    //     setWatchlist(updatedWatchlist);
    // };

    return (
        <Container fluid class="border border-secondary rounded">
            <Row>
                {watchlist.map((item, index) => (
                            <WatchlistItem item={item} />
                ))}
                {/* For reference*/}
                {/* <table class="table">
                    <tbody>
                        {watchlist.map((item, index) => (
                            <tr key={index} className="text-start align-middle">
                                <td scope="row">{item.name}</td>
                                <td>{item.current_price || 'N/A'}</td>
                                <td>
                                    <button onClick={() => handleRemoveItem(index)} class="btn btn-link">Remove</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table> */}
            </Row>
        </Container>
    );
};

export default Watchlist;