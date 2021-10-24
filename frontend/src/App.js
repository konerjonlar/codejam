import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      skillList: [],
      modal: false,
      activeItem: {
        name: "",
        tag:"",
        description: "",
      },
    };
  }
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/skill/")
      .then((res) => this.setState({ skillList: res.data }))
      .catch((err) => console.log(err));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();
    if (item.id) {
      axios
        .put(`/api/skill/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/api/skill/", item)
      .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/skill/${item.id}/`)
      .then((res) => this.refreshList());
  };


    
  createItem = () => {
    const item = { name: "",logo:"x", description: ""};

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
 
  renderItems = () => {
    
    const newItems = this.state.skillList

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`skill-name mr-2 `}
          name={item.description}
        >
          {item.name}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">skill app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add skill
                </button>
              </div>
             
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;