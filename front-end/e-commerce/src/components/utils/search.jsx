import { useEffect, useState } from 'react'
import { DecodeCars } from './carData/cars'
import { motion } from 'framer-motion'
import { useNavigate } from 'react-router-dom'

function Search() {
   const [newT, setNew] = useState(true)
   const navigate = useNavigate()
   const [usedT, setUsed] = useState(false)
   const [searchData, setSearchData] = useState({
      make: 'Tesla',
      model: 'Model 3',
      minPrice: '',
      maxPrice: '',
      new: true,
      used: false
   })
   const [colo, setColo] = useState(false)
   const [carModel, setCarModel] = useState()
   const [carList, setCarList] = useState()
   const [loadin, setLoading] = useState(false)
   const [show, setShow] = useState(false)
   const [searchModel, setSearchModel] = useState()

   const changeNew = () => {
      setSearchData({ ...searchData, "new": true, "used": false})
      setNew(true)
      setUsed(false)
   }
   const changeUsed = () => {
      setSearchData({ ...searchData, "used": true, "new": false})
      setUsed(true)
      setNew(false)
   }
   const handleMake = (event) => {
      setSearchData({ ...searchData, [event.target.name]: event.target.value, model: ''})
      setCarModel(searchModel.carModels[event.target.value])
      setColo(false)
   }
   const handleSearchData = (event) => {
      setColo(false)
      setSearchData({ ...searchData, [event.target.name]: event.target.value})
   }
   const handleSubmit = () => {
      event.preventDefault()
      setTimeout(() => {
         if (searchData.model != '' )
         {
            localStorage.setItem('searchData', JSON.stringify(searchData))
            navigate('/search_result')
         }
         else {
            setColo(true)
         }
         setLoading(false)
      }, 1000)
   }

   useEffect(() => {
      const fetchData = async () => {
         let response = DecodeCars()
         if (response) {
               setCarList(response[0].carLists)
               setSearchModel(response[0])
               setCarModel(response[0].carModels[response[0].carLists[0]])
               setShow(true)
            }
      }
      fetchData()
   }, [])

   const rotateVariant = {
      final: {
         rotate: 360,
      }
   }

  return (
   <form 
      noValidate
      onSubmit={handleSubmit} 
      className='flex w-[280px] flex-col gap-3  py-3 font-main px-5 border border-white rounded-lg bg-white shadow-lg shadow-blue-950'>
      <div 
         className='flex gap-0 border rounded-lg border-blue-600'>
         <button  
            className={`rounded-l-lg ${newT ? 'text-white bg-blue-600' : 'bg-white text-blue-600'} border-0 py-1.5 focus:border-0 font-medium text-xs w-[150px]`} type="button" onClick={changeNew}>
            New Car  
         </button>
         <button 
            className={` font-medium  rounded-r-lg border-0 py-1.5 focus:border-0 w-[150px] text-xs ${usedT ? 'text-white bg-blue-600' : 'bg-white text-blue-600'}`} type="button" onClick={changeUsed}>
            Used Car
         </button>
      </div>
      <div 
         className='flex flex-col py-1 items-start  rounded-md border border-gray-300 gap-1'>
         <label 
            htmlFor='make' className=' px-2 text-[10px] font-semibold  text-blue-950'>
            Select Make
         </label>
         <select 
            className='text-blue-950 block w-full focus:ring-blue-600 rounded-md focus:outline-none text-xs px-1 font-semibold' 
            name="make" 
            id="make" 
            onChange={handleMake}>
            {
               show && carList.map((car, index) => (
                  <option value={car} key={`${car}-${index}`}>
                     {car}
                  </option>
               ))
            }
         </select>
      </div>
      <div
          className={`flex flex-col py-1 items-start  rounded-md border border-gray-300 gap-1 ${ colo ? 'border border-red-500' : ''}`}>
         <label 
            htmlFor='model' className='px-2 text-[10px] font-semibold  text-blue-950'>
            Select Model
         </label>
         <select 
            className='px-1 block w-full focus:ring-blue-600 rounded-md  focus:outline-none text-blue-950 text-xs font-semibold' 
            name="model" 
            id="model"
            onChange={handleSearchData}>
            {
               show && carModel.map((car, index) => (
                  <option value={car} key={`${car}-${index}}`}>
                     {car}
                  </option>
               ))
            }
         </select>
      </div>
      <div 
         className='flex flex-col gap-1'>
         <p 
             className='px-2 text-[12px] font-semibold  text-blue-950'>
            Set Price(&#8358;)
         </p>
         <div className='px-3 flex py-2 items-start  rounded-md border border-gray-300 gap-1 justify-evenly'>
            <label
               className='text-[10px] font-semibold'
               htmlFor="minPrice">Minimum
               <input 
                  type="number" 
                  name="minPrice" 
                  id="minPrice" 
                  autoFocus
                  value={searchData.minPrice}
                  placeholder='2,000,000'
                  onChange={handleSearchData}
                  className='font-price text-xs border border-gray-400 focus:border-blue-600 px-1 py-1 font-medium placeholder:text-gray-600 
                  placeholder:text-xs placeholder:font-normal focus:border-2 focus:outline-none w-[100px] rounded-md' />
            </label>
            <label
               className='text-[10px] font-semibold'
               htmlFor="maxPrice"> Maximum
               <input 
                  type="number" 
                  name="maxPrice" 
                  id="maxPrice" 
                  value={searchData.maxPrice} 
                  placeholder='10,000,000'
                  onChange={handleSearchData}
                  className='font-price text-xs appearance-none border border-gray-400 focus:border-blue-600 px-1 py-1 font-medium placeholder:text-gray-600 placeholder:text-xs placeholder:font-normal focus:border-2 focus:outline-none w-[100px] rounded-md' />
            </label>
         </div>
      </div>
      <motion.button 
         type="submit"
          className=' bg-blue-600 border flex justify-center items-center font-extrabold w-100 text-white rounded-xl p-2' 
          onClick={() => {setLoading(true)}}>
            {
                     !loadin && <span>Find Car</span>
                  }
                  {
                     loadin && <motion.div variants={rotateVariant} animate="final" transition= {{
                        repeat: Infinity,
                        ease: 'linear',
                        duration: 0.3
                     }}
                     className='w-4 p-1 h-4 border-t-2 border-b-2 border-solid border-r-0 border-red border-l-2 rounded-full'></motion.div>
                  }
            </motion.button>

   </form>
  )
}

export default Search
