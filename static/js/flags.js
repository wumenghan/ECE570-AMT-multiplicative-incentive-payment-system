$(document).ready(function(){

	var Instruction = React.createClass({
		render: function(){
			return(
				<div className="instruction">
					<div className="instruction-header">
						<h1> Instruction</h1>
					</div>
					<div className="instruction-content">
						<p>There are flags of various countries below. <br/>	 
							For each flag, mark the continent to which the country belongs.<br/>
						If you are not sure about any answer, plase mark "I'm not sure".<br/>
						You <span style={{color:"red"}}>need to mark</span> at least something for every questions, otherwise your work will be <span style={{color:"red"}}>rejected</span>.	</p>
					</div>
				</div>
			);
		}

	});

	var Bonus = React.createClass({
		
		staticBar:function(fixmeTop){
			$(window).scroll(function(){
				var currentScroll = $(window).scrollTop();
			    if (currentScroll >= fixmeTop) {
			        $(".bonus-notification").css({
			            position: 'fixed',
			            top: '0',
			            left: '1.5em'
			        });
			    } else {
			        $(".bonus-notification").css({
			            position: 'static'
			        });
			    }
			});
			
		},
		componentDidMount: function(){
			var fixmeTop = $(this.refs.notification).offset().top;
			this.staticBar(fixmeTop);
		},
		render: function(){
			let notification;
			if(mode=="base"){
				notification = <div className="bonus-notification" ref="notification"></div>;
			}else{
				notification = <div className="bonus-notification" ref="notification">
						Note: An incorrect answer will make the bonus ZERO, so use the "I'm not sure" option wisely!
					</div> 
			}
			return (
				<div className="bonus">
					<div className="bonus-header">
						<h1>Bonus</h1>
					</div>
					<div className="bonus-content">
						<p>You start with 5 cents of bonus. <br/>
						There are some questions whose answers are known to us.<br/>
						For each of these questions if you answer <span className="bonus-blue"> correctly</span>, your bonus <span className="bonus-blue"> will be DOUBLED</span> (thus, you can earn upto <span className="bonus-green"> upto 40 cents as bonus</span>).<br/>
						If answer of any of these questions are <span className="bonus-red"> WRONG</span>, your bonus will become <span className="bonus-red"> ZERO</span>.<br/>
						Therefore, for questions you are not sure of, mark the <span className="bonus-blue">I'm not sure</span> option. This does not affect the bonus. </p>
					</div>
					{notification}	
				</div>
				);

		}
	});

	var Choice = React.createClass({

		getInitialState:function(){
			var id = this.props.id;
			if (mode == "base"){
				var choice = ["Africa", "Asia/Oceania", "Europe", "Neither of the above"];
			}else{
				var choice = ["Africa", "Asia/Oceania", "Europe", "Neither of the above", "I'm not sure"];
			}
			return {id:id, choice:choice};
		},
		translate: function(input){
			var dict = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"};
			return dict[input];
		},
		render:function(){
			return(
				<div id={this.state.id}>
					{this.state.choice.map(function(data, index){
						return(
							<div key={index}>
								<input type={'radio'} name={'task' + this.state.id} value={this.translate(index)}  id={'radio' + this.state.id + index}/> <label htmlFor={'radio' + this.state.id +index}> {data}</label>
							</div>
							);
					}, this)}
				</div>
				);

		}
	})

	var Content = React.createClass({

		getInitialState: function(){
			return {data:this.genList(1,20)};
		},
		genList: function(start, end){
			var list = [];
			for (var i=start; i<=end; i++){
				list.push(i);
			}
			return list;
		},
		render: function(){
			return(
				<div className="content">
					<div className="content-header">
					</div>
					<div className="content-content row" >
						{this.state.data.map(function(data, index){
							return(
								<div key={index} className="col s3">
									<img src={"./static/source/" + (index+1) + ".gif"}/>
									<Choice id={index} />
								</div>
							);
						})}
					</div>
				</div>

				);

		}

	});

	var Task = React.createClass({
		render: function(){
			return(
				<div className="">
					<Instruction />
					<Bonus />
					<form method={"get"} action={turkSubmitTo+"/mturk/externalSubmit"}>
						<Content />
						<input type={"hidden"} name={"assignmentId"} value={assignmentId} />
						<input type={"submit"} id="submit" className="waves-effect waves-light btn" value="submit" style={{float:"right"}}/>
					</form>

				</div>

				);
		}

	});

	ReactDOM.render(
		<Task />,
		document.getElementById("content")
	);
	if (assignmentId == "ASSIGNMENT_ID_NOT_AVAILABLE") {
		$("#submit").prop("disabled", true);
	}

});


