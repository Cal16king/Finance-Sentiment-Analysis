// Firebase app and Firestore setup
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs, query, orderBy } from 'firebase/firestore';

// Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyBJ9XIpX-MmqJKx1o00i5QOxXsX94EVP5U',
  authDomain: 'digit-210.firebaseapp.com',
  projectId: 'digit-210',
  storageBucket: 'digit-210.appspot.com',
  messagingSenderId: '606166340795',
  appId: '1:606166340795:web:ba5682cd98c3b53f02459e',
  measurementId: 'G-M62NC5GXC2',
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

// Create a query to retrieve articles ordered by date
const articlesQuery = query(collection(db, 'articles'), orderBy('date', 'asc'));

// Function to fetch and print all articles ordered by date
async function getArticles() {
  try {
    // Get all articles from Firestore
    const querySnapshot = await getDocs(articlesQuery);

    // Loop through each document and print the article information
    querySnapshot.forEach((doc) => {
      const data = doc.data(); // Get document data
      console.log('Article:', {
        text: data.text,
        date: data.date,
        sentiment: data.compound,
      });
    });
  } catch (error) {
    console.error('Error retrieving articles:', error);
  }
}

// Call the function to fetch articles
getArticles();
