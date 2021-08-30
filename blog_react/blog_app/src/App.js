import React, { useEffect, useState } from 'react';
import './App.css';
import Posts from './components/Posts';
import PostLoadingComponent from './components/PostLoading';
import axiosInstance from './axios';
function App() {
  const PostLoading = PostLoadingComponent(Posts);
  const [appState, setAppState] = useState({
    loading: false,
    posts: [],
  });

  useEffect(() => {
    setAppState({ loading: true });
    // fetch(apiUrl)
    //   .then((data) => data.json())
    //   .then((posts) => {
    //     if(!posts.detail){
    //       setAppState({ loading: false, posts: posts });
    //     }
    //   }).catch((err) => {
    //     //console.error(err);
    //   });

    axiosInstance.get(`/`)
    .then((res) => {
        if(!res.detail){
            setAppState({ loading: false, posts: res.data });
        }
    });

  }, [setAppState]);
  return (
    <div className="App">
      <h1>Latest Posts</h1>
      <PostLoading isLoading={appState.loading} posts={appState.posts} />
    </div>
  );
}
export default App;