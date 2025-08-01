import { useState } from 'react';
import Select from 'react-select';

const Searchbox = () => {
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