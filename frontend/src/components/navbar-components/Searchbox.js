import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Select from 'react-select';

const Searchbox = () => {
    const navigate = useNavigate();
    const searchOptions = [
        {value: "GOOGL", label: "Google"},
        {value: "AAPL", label: "Apple"},
        {value: "AMZN", label: "Amazon"},
        {value: "MSFT", label: "Microsoft"},
        {value: "TSLA", label: "Tesla"},
        {value: "FB", label: "Facebook"},
        {value: "NFLX", label: "Netflix"},
    ];
    
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
          className="w-30"
          placeholder="Search"
          isClearable
          isSearchable
        />
    );
}

export default Searchbox;