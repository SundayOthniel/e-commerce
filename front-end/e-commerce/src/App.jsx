import { BrowserRouter, Route, Routes } from "react-router-dom"
import ErrorPage from "./components/pages/errorpage"
import Home from "./components/pages/home"
import AllTypes from "./components/pages/types/alltypes"
import AllBrands from "./components/pages/brands/allbrands"
import AllListings from "./components/pages/listings/all_listings"
import FindaCar from "./components/pages/search/find"
import SearchResult from "./components/pages/search/search_result"
import Brand from "./components/pages/brands/brand_result"
import Type from "./components/pages/types/type_result"

function App() {
   return (
      <BrowserRouter
      basename={import.meta.env.DEV ? '/' : '/e-commerce_project/'}
      >
         <Routes>
            <Route path="*" element={<ErrorPage />} />
            <Route path="/" element={<Home />} />
            <Route path="cartypes" element={<AllTypes />} />
            <Route path="carbrands" element={<AllBrands />} />
            <Route path="featured" element={<AllListings />} />
            <Route path="find" element={<FindaCar />} />
            <Route path="search_result" element={<SearchResult />} />
            <Route path="brands" element={<Brand />} />
            <Route path="types" element={<Type />} />
         </Routes>
      </BrowserRouter>
   )
}

export default App
