import 'bootstrap/dist/css/bootstrap.css'
import DocumentProvider from '@/context/DocumentContext';
export const metadata = {
  title: "Invoice Generator",
  description: "mile of Threads Invoice Service",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <DocumentProvider>
        <body>{children}</body>

      </DocumentProvider>
    </html>
  );
}
