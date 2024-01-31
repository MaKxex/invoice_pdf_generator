"use client"
import { createContext, useContext, useState } from 'react';

const DocumentContext = createContext();

export const useDocumentContext = () => {
  return useContext(DocumentContext);
};

const DocumentProvider = ({ children }) => {
  const current_date = new Date();
  const current_date_plus_week = new Date(current_date.getTime() + 7 * 24 * 60 * 60 * 1000);

  const date_stamp_string = current_date.toLocaleDateString("en-GB");
  const new_date_stamp_string = current_date_plus_week.toLocaleDateString("en-GB");

  const [documentData, setDocumentData] = useState({
    money_sign: "€",
    is_invoice: false,
    is_private: false,
    document_num: "",
    document_type: "",
    privateField: "",
    company_name: "",
    register_number: 0,
    street: "",
    bank_name: "",
    bank_index: "",
    bank_billing: "",
    buyer_name: "",
    buyer_register_num: 0,
    buyer_mobile_num: "",
    buyer_email: "",
    delivery_type: "",
    payment_type: "",
    shipping_adress: "",
    product_rows: [],
    temp_price: 0,
    extras: [],
    total_price: 0,
    pay_before_date: new_date_stamp_string,
    dateStamp: date_stamp_string
  });
  
  
  const value = {
    documentData, 
    setDocumentData
  }


  return (
    <DocumentContext.Provider value={value}>
      {children}
    </DocumentContext.Provider>
  );
};

export default DocumentProvider;

