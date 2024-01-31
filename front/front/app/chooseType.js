"use client"

import { useDocumentContext } from "@/context/DocumentContext";

export function ChooseTypePage() {
    const { documentData, setDocumentData } = useDocumentContext();
    console.log(documentData );
    // Используйте documentData в вашем компоненте
    
    // Можете также использовать setDocumentData для обновления данных

    return (
        <section>
            <header>
                <div className="d-flex align-items-center justify-content-center h-100">
                    <div className="d-flex flex-column">
                        <div className="form-check">
                            <input className="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" />
                            <label className="form-check-label" for="flexRadioDefault1">
                                Private
                            </label>
                        </div>
                        <div className="form-check">
                            <input className="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked />
                            <label className="form-check-label" for="flexRadioDefault2">
                                Business
                            </label>
                        </div>
                        <button type="button" className="btn btn-primary">Submit</button>
                    </div>
                </div>
            </header>
        </section>
    );
}
