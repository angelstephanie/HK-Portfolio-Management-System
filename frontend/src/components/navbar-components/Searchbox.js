import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Select from 'react-select';

const Searchbox = () => {
    const navigate = useNavigate();
    const [searchOptions, setSearchOptions] = useState([]);

    useEffect(() => {
        // Fetch search options 
        fetch('http://127.0.0.1:5000/assets')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const options = data.map(item => ({ value: item.symbol, label: item.name }));
                setSearchOptions(options);
            })
            .catch(error => {
                console.error('Error fetching search options:', error);
            });
    }, []);
    
    const [selectedOption, setSelectedOption] = useState(null);
    const handleChange= (selectedOption) => {
        setSelectedOption(selectedOption);
        if (selectedOption != null) {
            const path = `/asset/${selectedOption.value}`;
            navigate(path);
        }
    }

    return (
        <Select
          options={searchOptions}
          value={selectedOption}
          onChange={handleChange}
          placeholder="Search"
          isClearable
          isSearchable
        />
    );
}

export default Searchbox;