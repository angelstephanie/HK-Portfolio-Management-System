const fs = require('fs');
const path = '/Hackathon/Sonia/HK-Portfolio-Management-System/frontend/src/assets/portfolio_performance.json';

// Generate dummy data for daily total asset value from January 1, 2024, to December 31, 2024
const startDate = new Date('2024-01-01');
const endDate = new Date('2024-12-31');
let currentDate = startDate;

const data = [];
let totalAssetValue = 100000; // Starting asset value

while (currentDate <= endDate) {
    // Random change between -1000 and +1000
    const randomChange = Math.floor(Math.random() * 2001) - 1000;
    totalAssetValue += randomChange;

    // Ensure totalAssetValue is not negative
    if (totalAssetValue < 0) totalAssetValue = 0;

    // Add entry to data
    data.push({
        date: currentDate.toISOString().split('T')[0], // Format date as YYYY-MM-DD
        totalAssetValue: totalAssetValue
    });

    // Move to the next day
    currentDate.setDate(currentDate.getDate() + 1);
}

// Save the generated data to the file
fs.writeFileSync(path, JSON.stringify(data, null, 4), 'utf8');
console.log('Dummy data generated and saved.');
