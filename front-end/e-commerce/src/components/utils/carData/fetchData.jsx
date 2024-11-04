async function FetchData() {
   const url = 'https://car-data.p.rapidapi.com/cars?limit=1&page=0';
   const options = {
      method: 'GET',
      headers: {
         'x-rapidapi-key': 'c747153925msh55c38d3237f0b5ep11bd9djsn569a5e24ab24',
         'x-rapidapi-host': 'car-data.p.rapidapi.com'
      }
   };

   try {
      const response = await fetch(url, options);
      if (!response.ok) {
         throw new Error(`HTTP error: Status ${response.status}`);
      }
      const result = await response.json();
      return result
   } catch (error) {
      console.error(error);
   }
}
export default FetchData
